from __future__ import print_function

from lime import lime_image, lime_text, lime_tabular
from aix360.algorithms.lbbe import LocalBBExplainer


class LimeTextExplainer(LocalBBExplainer):
    """
    Class that wraps lime_text.LimeTextExplainer [#]_
    For accessing any variables/functions not exposed by this class, please
    access them via the 'explainer' object variable initialized in '__init__' function.

    References:
        .. [#] `https://github.com/marcotcr/lime`_
    """

    def __init__(self, *argv, **kwargs):
        """
        Initialize lime text explainer object.
        """
        super(LimeTextExplainer, self).__init__(*argv, **kwargs)

        self.explainer = lime_text.LimeTextExplainer(*argv, **kwargs)

    def set_params(self, *argv, **kwargs):
        """
        Optionally, set parameters for the explainer.
        """
        pass

    def explain_instance(self, *argv, **kwargs):
        """
        Explains an input instance x.
        """
        self.explanation = self.explainer.explain_instance(*argv, **kwargs)

        return (self.explanation)


class LimeImageExplainer(LocalBBExplainer):
    """
    Class that wraps lime_image.LimeImageExplainer [#]_
    For accessing any variables/functions not exposed by this class, please
    access them via the 'explainer' object variable initialized in '__init__' function.

    References:
        .. [#] `https://github.com/marcotcr/lime`_
    """

    def __init__(self, *argv, **kwargs):
        """
        Initialize lime Image explainer object
        """
        super(LimeImageExplainer, self).__init__(*argv, **kwargs)

        self.explainer = lime_image.LimeImageExplainer(*argv, **kwargs)

    def set_params(self, *argv, **kwargs):
        """
        Optionally, set parameters for the explainer.
        """
        pass

    def explain_instance(self, *argv, **kwargs):
        """
        Explains and input instance x.
        """
        self.explanation = self.explainer.explain_instance(*argv, **kwargs)

        return (self.explanation)


class LimeTabularExplainer(LocalBBExplainer):
    """
    Class that wraps lime_image.LimeTabularExplainer [#]_
    For accessing any variables/functions not exposed by this class, please
    access them via the 'explainer' object variable initialized in '__init__' function.

    References:
        .. [#] `https://github.com/marcotcr/lime`_
    """

    def __init__(self, *argv, **kwargs):
        """
        Initialize lime Image Tabular object
        """
        super(LimeTabularExplainer, self).__init__(*argv, **kwargs)

        self.explainer = lime_tabular.LimeTabularExplainer(*argv, **kwargs)

    def set_params(self, verbose=0):
        """
        Optionally, set parameters for the explainer.
        """
        pass

    def explain_instance(self, *argv, **kwargs):
        """
        Explains an input instance x.
        """
        self.explanation = self.explainer.explain_instance(*argv, **kwargs)

        return (self.explanation)