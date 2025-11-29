def png_to_svg(input_path, output_path):
    """Raster to vector conversion is not supported."""
    return "不支持的转换：无法将光栅图像 (PNG) 转换为矢量图像 (SVG)。"

def svg_to_png(input_path, output_path):
    """Vector to raster conversion requires a dedicated rendering library."""
    return "不支持的转换：SVG 渲染需要专门的库 (如 'cairosvg')。"
