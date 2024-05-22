from pymonntorch import Behavior, NeuronGroup
import torch


class InputBehavior(Behavior):

    def initialize(self, ng: NeuronGroup) -> None:
        self.spikes = self.parameter('spikes', required=True)

        ng.spike = self.spikes[ng.network.iteration, :ng.size]
        ng.spike_counts = ng.spike

    def forward(self, ng: NeuronGroup) -> None:
        ng.spike = self.spikes[ng.network.iteration, :ng.size]
        ng.spike_counts += ng.spike
