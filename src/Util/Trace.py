from pymonntorch import Behavior


class SpikeTrace(Behavior):
    """
    Calculates the spike trace.

    Note : should be placed after Fire behavior.

    Args:
        tau_s (float): decay term for spike trace. The default is None.
    """

    def __init__(self, tau_s, *args, **kwargs):
        super().__init__(*args, tau_s=tau_s, **kwargs)

    def initialize(self, neurons):
        """
        Sets the trace attribute for the neural population.
        """
        self.tau_s = self.parameter("tau_s", None, required=True)
        neurons.trace = neurons.vector(0.0)

    def forward(self, neurons):
        """
        Calculates the spike trace of each neuron by adding current spike and decaying the trace so far.
        """
        neurons.trace += neurons.spike
        neurons.trace -= (neurons.trace / self.tau_s) * neurons.network.dt
