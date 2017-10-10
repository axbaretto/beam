#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""SDK Fn Harness entry point."""

import logging
import os
import sys

from google.protobuf import text_format

from apache_beam.portability.api import endpoints_pb2
from apache_beam.runners.worker.log_handler import FnApiLogRecordHandler
from apache_beam.runners.worker.sdk_worker import SdkHarness

# This module is experimental. No backwards-compatibility guarantees.


def main(unused_argv):
  """Main entry point for SDK Fn Harness."""
  if 'LOGGING_API_SERVICE_DESCRIPTOR' in os.environ:
<<<<<<< HEAD
    logging_service_descriptor = endpoints_pb2.ApiServiceDescriptor()
=======
    logging_service_descriptor = beam_fn_api_pb2.ApiServiceDescriptor()
>>>>>>> 5046e97cfe1745620685907907377c6a35cd104c
    text_format.Merge(os.environ['LOGGING_API_SERVICE_DESCRIPTOR'],
                      logging_service_descriptor)

    # Send all logs to the runner.
    fn_log_handler = FnApiLogRecordHandler(logging_service_descriptor)
    # TODO(vikasrk): This should be picked up from pipeline options.
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(fn_log_handler)
  else:
    fn_log_handler = None

  try:
    logging.info('Python sdk harness started.')
    service_descriptor = endpoints_pb2.ApiServiceDescriptor()
    text_format.Merge(os.environ['CONTROL_API_SERVICE_DESCRIPTOR'],
                      service_descriptor)
    # TODO(robertwb): Support credentials.
    assert not service_descriptor.oauth2_client_credentials_grant.url
    SdkHarness(service_descriptor.url).run()
    logging.info('Python sdk harness exiting.')
  except:  # pylint: disable=broad-except
    logging.exception('Python sdk harness failed: ')
    raise
  finally:
    if fn_log_handler:
      fn_log_handler.close()


if __name__ == '__main__':
  main(sys.argv)
