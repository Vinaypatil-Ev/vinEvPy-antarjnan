import torch
import tensorflow as tf
import numpy as np


def is_torch_tensor(x):
    return torch.is_tensor(x)


def is_tf_tensor(x):
    return tf.is_tensor(x)


def is_nparray(x):
    return isinstance(x, np.ndarray)


def tf_to_torch(x):
    pass


def torch_to_tf(x):
    pass


def return_torch_tensor(ten, dtype):
    if isinstance(ten, list):
        tensor = torch.tensor(ten, dtype=dtype)
        if tensor.dim() == 1:
            tensor = tensor.view(-1, 1)
        return tensor
    elif is_tf_tensor(ten):
        return tf_to_torch(ten)
    elif is_nparray(ten):
        tensor = torch.from_numpy(ten, dtype=dtype)
        if tensor.dim() == 1:
            tensor = tensor.view(-1, 1)
        return tensor
    else:
        return ten


def return_tf_tensor(ten, dtype):
    if isinstance(ten, list):
        pass
    elif is_torch_tensor(ten):
        return torch_to_tf(ten)
    elif is_nparray(ten):
        pass
    else:
        return ten
