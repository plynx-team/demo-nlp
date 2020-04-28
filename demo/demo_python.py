from plynx.plugins.executors import local


class DemoPythonNode(local.PythonNode):
    def __init__(self, *args, **argv):
        super(DemoPythonNode, self).__init__(*args, **argv)
