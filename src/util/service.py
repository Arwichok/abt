from __future__ import annotations

import abc
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .container import Container



@dataclass
class Service(abc.ABC):
    ct: Optional[Container] = None
