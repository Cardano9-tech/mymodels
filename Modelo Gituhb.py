name: "SIMPNET"
##########################
#Put Your DataLayers Here#
##########################
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}

layer {
  name: "bn1"
  type: "BatchNorm"
  bottom: "conv1"
  top: "conv1"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
    include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn1"
  type: "BatchNorm"
  bottom: "conv1"
  top: "conv1"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
    include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale1"
  type: "Scale"
  bottom: "conv1"
  top: "conv1"
  scale_param {
    bias_term: true
  }
}

layer {
  name: "relu1"
  type: "ReLU"
  bottom: "conv1"
  top: "conv1"
}
#######DropOut##########
layer {
 name: "drop2_1"
 type: "Dropout"
 bottom: "conv1"
 top: "conv1"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv1_0"
  type: "Convolution"
  bottom: "conv1"
  top: "conv1_0"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 128
    pad: 1
    kernel_size: 3
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}
layer {
  name: "bn1_0"
  type: "BatchNorm"
  bottom: "conv1_0"
  top: "conv1_0"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
    include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn1_0"
  type: "BatchNorm"
  bottom: "conv1_0"
  top: "conv1_0"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
    include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale1_0"
  type: "Scale"
  bottom: "conv1_0"
  top: "conv1_0"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu1_0"
  type: "ReLU"
  bottom: "conv1_0"
  top: "conv1_0"
}
#######DropOut##########
layer {
 name: "drop1_0"
 type: "Dropout"
 bottom: "conv1_0"
 top: "conv1_0"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "conv1_0"
  top: "conv2"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
  }
}
layer {
  name: "bn2"
  type: "BatchNorm"
  bottom: "conv2"
  top: "conv2"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
  
}
layer {
  name: "bn2"
  type: "BatchNorm"
  bottom: "conv2"
  top: "conv2"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
  
}
layer {
  name: "scale2"
  type: "Scale"
  bottom: "conv2"
  top: "conv2"
  scale_param {
    bias_term: true
  }
}

layer {
  name: "relu2"
  type: "ReLU"
  bottom: "conv2"
  top: "conv2"
}
#######DropOut##########
layer {
 name: "drop2_0"
 type: "Dropout"
 bottom: "conv2"
 top: "conv2"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv2_1"
  type: "Convolution"
  bottom: "conv2"
  top: "conv2_1"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
  }
}
layer {
  name: "bn2_1"
  type: "BatchNorm"
  bottom: "conv2_1"
  top: "conv2_1"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn2_1"
  type: "BatchNorm"
  bottom: "conv2_1"
  top: "conv2_1"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale2_1"
  type: "Scale"
  bottom: "conv2_1"
  top: "conv2_1"
  scale_param {
    bias_term: true
  }
}

layer {
  name: "relu2_1"
  type: "ReLU"
  bottom: "conv2_1"
  top: "conv2_1"
}
layer {
  name: "pool2_1"
  type: "Pooling"
  bottom: "conv2_1"
  top: "pool2_1"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
#######DropOut##########
layer {
 name: "drop2_1"
 type: "Dropout"
 bottom: "pool2_1"
 top: "pool2_1"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv2_2"
  type: "Convolution"
  bottom: "pool2_1"
  top: "conv2_2"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "gaussian"
      std: 0.01
    }
  }
}
layer {
  name: "bn2_2"
  type: "BatchNorm"
  bottom: "conv2_2"
  top: "conv2_2"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn2_2"
  type: "BatchNorm"
  bottom: "conv2_2"
  top: "conv2_2"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale2_2"
  type: "Scale"
  bottom: "conv2_2"
  top: "conv2_2"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu2_2"
  type: "ReLU"
  bottom: "conv2_2"
  top: "conv2_2"
}
#######DropOut##########
layer {
 name: "drop2_2"
 type: "Dropout"
 bottom: "conv2_2"
 top: "conv2_2"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv3"
  type: "Convolution"
  bottom: "conv2_2"
  top: "conv3"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 128
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}
layer {
  name: "bn3"
  type: "BatchNorm"
  bottom: "conv3"
  top: "conv3"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn3"
  type: "BatchNorm"
  bottom: "conv3"
  top: "conv3"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale3"
  type: "Scale"
  bottom: "conv3"
  top: "conv3"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu3"
  type: "ReLU"
  bottom: "conv3"
  top: "conv3"
}
#######DropOut##########
layer {
 name: "drop3"
 type: "Dropout"
 bottom: "conv3"
 top: "conv3"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv4"
  type: "Convolution"
  bottom: "conv3"
  top: "conv4"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}
layer {
  name: "pool4"
  type: "Pooling"
  bottom: "conv4"
  top: "pool4"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "bn4"
  type: "BatchNorm"
  bottom: "pool4"
  top: "pool4"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn4"
  type: "BatchNorm"
  bottom: "pool4"
  top: "pool4"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale4"
  type: "Scale"
  bottom: "pool4"
  top: "pool4"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu4"
  type: "ReLU"
  bottom: "pool4"
  top: "pool4"
}
#######DropOut##########
layer {
 name: "drop4"
 type: "Dropout"
 bottom: "pool4"
 top: "pool4"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv4_1"
  type: "Convolution"
  bottom: "pool4"
  top: "conv4_1"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}
layer {
  name: "bn4_1"
  type: "BatchNorm"
  bottom: "conv4_1"
  top: "conv4_1"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn4_1"
  type: "BatchNorm"
  bottom: "conv4_1"
  top: "conv4_1"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale4_1"
  type: "Scale"
  bottom: "conv4_1"
  top: "conv4_1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu4_1"
  type: "ReLU"
  bottom: "conv4_1"
  top: "conv4_1"
}
#######DropOut##########
layer {
 name: "drop4_1"
 type: "Dropout"
 bottom: "conv4_1"
 top: "conv4_1"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "conv4_2"
  type: "Convolution"
  bottom: "conv4_1"
  top: "conv4_2"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 256
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}
layer {
  name: "bn4_2"
  type: "BatchNorm"
  bottom: "conv4_2"
  top: "conv4_2"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn4_2"
  type: "BatchNorm"
  bottom: "conv4_2"
  top: "conv4_2"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale4_2"
  type: "Scale"
  bottom: "conv4_2"
  top: "conv4_2"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu4_2"
  type: "ReLU"
  bottom: "conv4_2"
  top: "conv4_2"
}
#######DropOut##########
layer {
 name: "drop4_2"
 type: "Dropout"
 bottom: "conv4_2"
 top: "conv4_2"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "pool4_2"
  type: "Pooling"
  bottom: "conv4_2"
  top: "pool4_2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
##########4_0##############
layer {
  name: "conv4_0"
  type: "Convolution"
  bottom: "pool4_2"
  top: "conv4_0"
  param {
    lr_mult: 1
  }
  convolution_param {
    num_output: 512
    kernel_size: 3
	pad: 1
    stride: 1
    bias_term: true
    weight_filler {
      type: "xavier"
    }
  }
}
layer {
  name: "bn4_0"
  type: "BatchNorm"
  bottom: "conv4_0"
  top: "conv4_0"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TRAIN
  }
    batch_norm_param {
    use_global_stats: false
    moving_average_fraction: 0.95
  }
}
layer {
  name: "bn4_0"
  type: "BatchNorm"
  bottom: "conv4_0"
  top: "conv4_0"
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  param {
    lr_mult: 0
	 decay_mult: 0
  }
  
      include {
    phase: TEST
  }
    batch_norm_param {
    use_global_stats: true
    moving_average_fraction: 0.95
  }
}
layer {
  name: "scale4_0"
  type: "Scale"
  bottom: "conv4_0"
  top: "conv4_0"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "relu4_0"
  type: "ReLU"
  bottom: "conv4_0"
  top: "conv4_0"
}
#######DropOut##########
layer {
 name: "drop4_0"
 type: "Dropout"
 bottom: "conv4_0"
 top: "conv4_0"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "cccp4"
  type: "Convolution"
  bottom: "conv4_0"
  top: "cccp4"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 2048
    kernel_size: 1
    group: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  name: "relu_cccp4"
  type: "ReLU"
  bottom: "cccp4"
  top: "cccp4"
}
#--------Dropout--------
#######DropOut##########
layer {
 name: "drop4_3"
 type: "Dropout"
 bottom: "cccp4"
 top: "cccp4"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
#-------------------------
layer {
  name: "cccp5"
  type: "Convolution"
  bottom: "cccp4"
  top: "cccp5"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 256
    kernel_size: 1
    group: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  name: "relu_cccp5"
  type: "ReLU"
  bottom: "cccp5"
  top: "cccp5"
}

layer {
  name: "poolcp5"
  type: "Pooling"
  bottom: "cccp5"
  top: "poolcp5"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
#######DropOut##########
layer {
 name: "drop4_5"
 type: "Dropout"
 bottom: "poolcp5"
 top: "poolcp5"
 dropout_param {
  dropout_ratio: 0.2
  }
 }
########################
layer {
  name: "cccp6"
  type: "Convolution"
  bottom: "poolcp5"
  top: "cccp6"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output:256
    kernel_size: 3
	pad: 1
    group: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  name: "relu_cccp6"
  type: "ReLU"
  bottom: "cccp6"
  top: "cccp6"
}

layer {
  name: "poolcp6"
  type: "Pooling"
  bottom: "cccp6"
  top: "poolcp6"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "poolcp6"
  top: "ip1"
  param {
    lr_mult: 1
    decay_mult: 0
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  inner_product_param {
    num_output: 10
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "accuracy"
  type: "Accuracy"
  bottom: "ip1"
  bottom: "label"
  top: "accuracy"
  include {
    phase: TEST
  }
}
layer {
  name: "accuracy_training"
  type: "Accuracy"
  bottom: "ip1"
  bottom: "label"
  top: "accuracy_training"
  include {
    phase: TRAIN
  }
}
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "ip1"
  bottom: "label"
  top: "loss"
}