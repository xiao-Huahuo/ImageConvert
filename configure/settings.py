file_types = [
    'jpg', 'jpeg', 'png', 'ico', 'bmp', 'webp', 'gif', 'heic', 'svg'
]

convert_loss = {
    # JPG/JPEG
    ('jpg', 'jpeg'): '几乎无损失',
    ('jpg', 'png'): '文件变大，质量提升不明显。PNG是无损格式，但无法恢复JPG已丢失的细节。',
    ('jpg', 'ico'): '会损失部分质量，且没有透明度。',
    ('jpg', 'bmp'): '几乎无损失，但文件体积会显著增大。',
    ('jpg', 'webp'): '质量和文件大小通常会优化，WebP压缩效率更高。',
    ('jpg', 'gif'): '会严重损失色彩（最多256色）和质量。',
    ('jpg', 'heic'): '可能保持相似质量和更小的文件大小。',

    # PNG
    ('png', 'jpg'): '损失透明度和质量。PNG的透明部分通常会变黑或变白。',
    ('png', 'jpeg'): '损失透明度和质量。',
    ('png', 'ico'): '理想的转换，透明度会被保留。',
    ('png', 'bmp'): '损失透明度，但保留图像质量。',
    ('png', 'webp'): '理想的转换，通常可以无损或有损压缩，并保留透明度。',
    ('png', 'gif'): '可能损失色彩（GIF最多256色），但保留简单透明度。',
    ('png', 'heic'): '保留高质量，并可能减小文件大小，透明度支持取决于HEIC变体。',

    # ICO
    ('ico', 'png'): '几乎无损失，透明度会被保留。',
    ('ico', 'jpg'): '会损失透明度和质量。',
    ('ico', 'jpeg'): '会损失透明度和质量。',

    # BMP
    ('bmp', 'jpg'): '有损压缩，文件变小，质量略微下降。',
    ('bmp', 'png'): '无损压缩，文件通常会变小，质量不变。',
    ('bmp', 'webp'): '高效压缩，文件显著变小，质量可控。',
    ('bmp', 'gif'): '严重损失色彩和质量。',

    # WebP
    ('webp', 'png'): '几乎无损失（如果WebP是无损格式），文件可能变大。',
    ('webp', 'jpg'): '有损转换，可能会损失透明度。',

    # GIF
    ('gif', 'png'): '保留单帧图像，色彩信息会被完整保留。',
    ('gif', 'jpg'): '保留单帧图像，并进行有损压缩。',

    # HEIC
    ('heic', 'jpg'): '通用格式，兼容性好，但质量可能略有下降。',
    ('heic', 'png'): '无损转换，保留完整质量，但文件会显著变大。',

    # SVG (不支持)
    ('svg', 'png'): '不支持的转换路径。SVG是矢量格式，需要专门的渲染库。',
    ('png', 'svg'): '不支持的转换路径。这是一个光栅到矢量的复杂过程。'
}

# 补充对称转换
symmetric_pairs = {}
for (t1, t2), desc in list(convert_loss.items()):
    if (t2, t1) not in convert_loss:
        symmetric_pairs[(t2, t1)] = desc

convert_loss.update(symmetric_pairs)
