# /********************************************************************************
# * Copyright (c) 2023 Contributors to the Eclipse Foundation
# *
# * See the NOTICE file(s) distributed with this work for additional
# * information regarding copyright ownership.
# *
# * This program and the accompanying materials are made available under the
# * terms of the Apache License 2.0 which is available at
# * http://www.apache.org/licenses/LICENSE-2.0
# *
# * SPDX-License-Identifier: Apache-2.0
# ********************************************************************************/

from typing import Any, Optional, Callable
import logging

from kuksa_client.grpc import DataType


log = logging.getLogger("datapoint")


class DataPoint:
    def __init__(
        self,
        path: str,
        data_type: DataType,
        value: Any,
        value_listener: Optional[Callable[[Any], None]] = None,
    ):
        self.path = path
        self.data_type = data_type
        self.value = value
        self.value_listener = value_listener

    def has_discrete_value_type(self):
        """Return if the datapoint has a discrete value type."""
        return self.data_type == DataType.BOOLEAN or self.data_type == DataType.STRING

    def set_value(self, new_value):
        """Set the value of the datapoint."""
        if self.value != new_value:
            self.value = new_value
            if self.value_listener is not None:
                self.value_listener(self)

    def __eq__(self, other):
        return (
            isinstance(other, DataPoint)
            and self.path == other.path
            and self.data_type == other.data_type
            and self.value == other.value
        )

    def __ne__(self, other):
        return not self.__eq__(other)
