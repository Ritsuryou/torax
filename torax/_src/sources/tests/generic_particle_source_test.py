# Copyright 2024 DeepMind Technologies Limited
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
from absl.testing import absltest
from torax._src.sources import generic_particle_source
from torax._src.sources.tests import test_lib


class SourceTest(test_lib.SingleProfileSourceTestCase):
  """Tests for GenericParticleSource."""

  def setUp(self):
    super().setUp(
        source_config_class=generic_particle_source.GenericParticleSourceConfig,
        source_name=generic_particle_source.GenericParticleSource.SOURCE_NAME,
    )


if __name__ == '__main__':
  absltest.main()
