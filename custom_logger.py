import logging
import sys

class CustomLogger:
    """A configured console logger with clear formatting."""
    
    @staticmethod
    def get_logger(name: str = "AppLogger", level: int = logging.INFO) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        # Prevent adding multiple handlers if called repeatedly
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(level)
            
            # Formater with timestamp, level name, and message
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
        return logger


# --- Example Usage ---
if __name__ == "__main__":
    log = CustomLogger.get_logger("PracticeLogger")
    
    log.info("Application initialized successfully.")
    log.warning("Configuration file missing defaults; using fallback values.")
    log.error("Failed to connect to database endpoint.")
