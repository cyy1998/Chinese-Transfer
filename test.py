import tensorflow as tf
from model import generate

saver=tf.train.import_meta_graph('./save/model.ckpt.meta')
gragh = tf.get_default_graph()# 获取当前图，为了后续训练时恢复变量
tensor_name_list = [tensor.name for tensor in gragh.as_graph_def().node]# 得到当前图中所有变量的名称
print(tensor_name_list)
