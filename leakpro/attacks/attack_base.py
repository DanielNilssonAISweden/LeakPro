"""Run optuna to find best hyperparameters."""
from abc import ABC, abstractmethod

from leakpro.utils.import_helper import Self


class AbstractAttack(ABC):
    """Abstract attack template for attack objects."""

    def get_configs(self: Self) -> dict:
        """Return configs used for attack."""
        return self.configs

    @abstractmethod
    def run_attack() -> None:
        """Run the attack on the target model and dataset.

        This method is implemented by subclasses (e.g., GIA and MIA attacks),
        each of which provides specific behavior and results.

        Returns
        -------
        Depends on the subclass implementation.

        """
        pass

