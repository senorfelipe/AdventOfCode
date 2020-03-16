"""--- Day 8: Space Image Format ---"""
import operator

input = open("input.txt").read()
image_data = [int(val) for val in list(input)]


def get_layers():
    layers = []
    last_split_idx = 0
    rows = []
    for i, digit in enumerate(image_data):
        if (i + 1) % 25 == 0:
            rows.append(image_data[last_split_idx:i + 1])
            last_split_idx = i + 1
        if len(rows) == 6:
            layers.append(rows.copy())
            rows.clear()
    return layers


def get_fewest_0_digits_layer():
    layers = get_layers()
    layer_0_dict = {}
    for layer_no, layer in enumerate(layers):
        layer_0_dict[layer_no] = 0
        for image in layer:
            layer_0_dict[layer_no] = layer_0_dict[layer_no] + image.count(0)
    return min(layer_0_dict.items(), key=operator.itemgetter(1))[0]


def result():
    layer = get_layers()[get_fewest_0_digits_layer()]
    ones, twos = 0, 0
    for image in layer:
        ones, twos = ones + image.count(1), twos + image.count(2)
    return ones * twos


# awnser 1
print(result())


def decode_image():
    images = get_images_per_layer(get_layers())
    decoded_row = []
    decoded_image = []
    for i in range(25 * 6):
        for j in range(len(images)):
            if 2 != images[j][i]:
                if len(decoded_row) == 25:
                    decoded_image.append(decoded_row.copy())
                    decoded_row.clear()
                decoded_row.append(images[j][i])
                break
    decoded_image.append(decoded_row)
    return decoded_image


def get_images_per_layer(layers):
    images = []
    raw_layer = []
    for layer in layers:
        for row in layer:
            for pixel in row:
                raw_layer.append(pixel)
        images.append(raw_layer.copy())
        raw_layer.clear()
    return images


def print_decoded():
    image = decode_image()
    for row in image:
        print(str(row).strip('[]').replace(', ', '').replace('0', '.'))


print_decoded()
