import tensorflow as tf
devices=tf.config.list_physical_devices('GPU')
if devices:
    print(f'\n{len(devices)} GPU  available')
    print(repr(devices[0]))
    device_name = devices[0].name.split('/physical_device:')[1]  # Extract "GPU:0" or similar
    try:
        memory_info = tf.config.experimental.get_memory_info(device_name)
        print(repr(memory_info))
    except ValueError as e:
        print(f"Error getting memory info: {e}")
        print(f"Device name used: {device_name}") # Print the device name to debug
else:
    print('GPU is not available')