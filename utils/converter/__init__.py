import importlib
import os

MODULE_MAPPING = {
    frozenset(['jpg', 'jpeg']): 'JPG__JPEG',
    frozenset(['jpg', 'png']): 'JPG__PNG',
    frozenset(['jpeg', 'png']): 'JPEG__PNG',
}

def convert_image(input_path, output_path, output_format, output_filename):
    """
    Dynamically finds and calls the correct conversion function.
    """
    if not os.path.exists(input_path):
        return "错误：输入文件不存在。"

    input_ext = os.path.splitext(input_path)[1].lower().replace('.', '')
    output_ext = output_format.lower()

    if input_ext == output_ext:
        # 如果文件名也相同，则无需转换
        base_name_input = os.path.splitext(os.path.basename(input_path))[0]
        if base_name_input == output_filename:
            return "输入和输出格式及文件名均相同，无需转换。"

    key = frozenset([input_ext, output_ext])
    module_name = MODULE_MAPPING.get(key)

    if not module_name:
        if input_ext in ('jpg', 'jpeg') and output_ext in ('jpg', 'jpeg'):
             module_name = 'JPG__JPEG'
        else:
            return f"错误：不支持从 {input_ext} 到 {output_ext} 的转换。"

    function_name = f"{input_ext}_to_{output_ext}"

    try:
        converter_module = importlib.import_module(f".{module_name}", package="utils.converter")
        convert_func = getattr(converter_module, function_name)
        
        # 使用用户指定的文件名构建输出路径
        full_output_path = os.path.join(output_path, f"{output_filename}.{output_ext}")

        return convert_func(input_path, full_output_path)

    except ImportError:
        return f"错误：找不到实现文件 '{module_name}.py'。"
    except AttributeError:
        return f"错误：在模块 {module_name} 中找不到转换函数 '{function_name}'。"
    except Exception as e:
        return f"转换过程中发生未知错误：{e}"
