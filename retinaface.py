import collections

import tensorflow as tf
import numpy as np

from absl import app, flags, logging
from retinaface_tf2.modules.models import RetinaFaceModel
from retinaface_tf2.modules.utils import (set_memory_growth, load_yaml, draw_bbox_landm,
                                           pad_input_image, recover_pad_output)

PredictRegion = collections.namedtuple("PredictRegion", ["x1", "y1", "x2", "y2"]);

class RetinaFace:
    def __init__(self, cfg_file, iou_th=0.4, score_th=0.5):
        logger = tf.get_logger()
        logger.disabled = True
        logger.setLevel(logging.FATAL)
        set_memory_growth()

        cfg = load_yaml(cfg_file)

        model = RetinaFaceModel(cfg, training=False, iou_th=iou_th,
                                score_th=score_th)
        checkpoint_dir = './checkpoints/' + cfg['sub_name']
        checkpoint = tf.train.Checkpoint(model=model)

        if tf.train.latest_checkpoint(checkpoint_dir):
            checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
            print("[*] load ckpt from {}.".format(
                tf.train.latest_checkpoint(checkpoint_dir)))
        else:
            print("[*] Cannot find ckpt from {}.".format(checkpoint_dir))
            exit()
        self.model = model
        self.cfg   = cfg

    ## input must be a image which is RGB scale
    def predict_img(self, img):
        [ height, width, channel ] = img.shape
        img, pad_params = pad_input_image(img, max_steps=max(self.cfg['steps']))
        outputs = self.model(img[np.newaxis, ...]).numpy()
        outputs = recover_pad_output(outputs, pad_params)
        return [ PredictRegion(int(out[0] * width), int(out[1] * height), int(out[2] * width), int(out[3] * height))
                                                                                    for out in outputs ]
