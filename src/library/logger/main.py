from datetime import datetime
from termcolor import colored, cprint


def get_debug_text(message):
  out_message=f'# {message}'
  if len(out_message) <= 88:
    length_diff = 88 - len(out_message)
    separators='='*length_diff
    out_message=f'{out_message} {separators}#'

  return out_message


class Logger:

  """
  Loggin Class.
  Logs has pattern [YYYY-MM-DD HH:MI:SS.SSSSSS] [Log Type] - Message
  Ex: [2020-05-04 10:23:50.121213] [WARNING] - My Log Message.

  Prefer using Class Log Types, due to printed colors.
  """

  ERROR = 'ERROR'
  INFO = 'INFO'
  WARNING = 'WARNING'
  DEBUG = 'DEBUG'

  @staticmethod
  def emit(message='', log_type='INFO'):
    out_message=message
    if Logger.DEBUG == log_type:
      out_message=get_debug_text(out_message)
    text = colored(f"[{datetime.now()}]  [{log_type}] - {out_message}")
    cprint(text, Logger._get_color(log_type))

  @staticmethod
  def _get_color(log_type):
    if Logger.ERROR == log_type:
        return 'red'
    elif Logger.WARNING == log_type:
        return 'yellow'
    else:
        return 'white'