# SecuML
# Copyright (C) 2016-2019  ANSSI
#
# SecuML is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# SecuML is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with SecuML. If not, see <http://www.gnu.org/licenses/>.

import numpy as np

from secuml.core.active_learning.strategies.random import Random as CoreRandom
from secuml.core.tools.plots.dataset import PlotDataset
from secuml.exp.active_learning.queries.random import RandomQueries


class Random(CoreRandom):

    def _set_queries(self):
        self.queries['random'] = RandomQueries(self.iteration,
                                               self.iteration.conf.batch)

    def get_url(self):
        secuml_conf = self.iteration.exp.exp_conf.secuml_conf
        return 'http://%s:%d/ilabAnnotations/%d/%d/' % (
                    secuml_conf.host, secuml_conf.port,
                    self.iteration.exp.exp_id, self.iteration.iter_num)

    def get_exec_times_header(self):
        header = ['binary_model']
        header.extend(CoreRandom.get_exec_times_header(self))
        return header

    def get_exec_times(self):
        line = [self.iteration.update_model.exec_time]
        line.extend(CoreRandom.get_exec_times(self))
        return line

    def exec_time_display(self):
        binary_model = PlotDataset(np.array([]), 'Binary model')
        v = [binary_model]
        v.extend(CoreRandom.get_exec_times_display(self))
        return v
