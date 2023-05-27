import logging
from config.configManager import console_logger, file_logger


'''
自定义日志类
'''
class Logger(object):
    def __init__(self,
                 logger_level=logging.INFO,
                 console_level=logging.INFO,
                 file_level=logging.INFO,
                 logger_format='%(asctime)s [%(name)s] [%(levelname)s] %(funcName)s: %(message)s'):
        self.logger_level = logger_level
        self.logger_format = logger_format
        self.console_level = console_level
        self.file_level = file_level
        
    '''创建日志'''
    def create_logger(self, logger_name, logger_file):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.logger_level)
        if console_logger:
            # 创建输出控制台日志
            self.create_console_logger(logger)
        if file_logger:
            # 创建文件输出日志
            self.create_file_logger(logger, logger_file)        
        return logger
    
    '''创建输出控制台日志'''
    def create_console_logger(self, logger):
        # 添加一个输出到控制台的处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.console_level)
        formatter = logging.Formatter(self.logger_format)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    '''创建输出文件日志'''
    def create_file_logger(self, logger, logger_file):
        # 添加一个输出到文件的处理器
        file_handler = logging.FileHandler(logger_file)
        file_handler.setLevel(self.file_level)
        formatter = logging.Formatter(self.logger_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)




logger = Logger(logger_level=logging.DEBUG)

# 创建 run_logger，用于记录运行日志
run_logger = logger.create_logger('run_log', 'log/run.log')
