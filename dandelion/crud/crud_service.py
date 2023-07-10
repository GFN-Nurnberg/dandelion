# Copyright 2022 99Cloud, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from dandelion.crud.base import CRUDBase
from dandelion.models import Service
from dandelion.schemas.service import ServiceCreate, ServiceUpdate


class CRUDService(CRUDBase[Service, ServiceCreate, ServiceUpdate]):
    """"""

    def get_by_name(self, db: Session, name: str) -> Service:
        return db.query(self.model).filter(self.model.name == name).first()

    def get_all(
        self,
        db: Session,
        name: Optional[str] = None,
    ) -> List[Service]:
        query_ = db.query(self.model)
        if name is not None:
            query_ = self.fuzz_filter(query_, self.model.name, name)
        return query_.all()


service = CRUDService(Service)
