from plynx.plugins.executors import dag
import plynx.db.node


class DemoDAG(dag.DAG):
    def __init__(self, *args, **argv):
        super(DemoDAG, self).__init__(*args, **argv)

    @classmethod
    def get_default_node(cls, is_workflow):
        node = super().get_default_node(is_workflow)
        nodes_parameter = node.parameters[0]

        null = None
        true = True
        false = False

        nodes_parameter.value.value = [
            plynx.db.node.Node.from_dict({
              "_id": "5e66fc2df1e5b88d18f5c14f",
              "title": "Word2Vec",
              "description": "Find similar words",
              "kind": "demo-python-node-operation",
              "parent_node_id": null,
              "successor_node_id": null,
              "original_node_id": "5e66fbef2fb8847bfdb495d1",
              "inputs": [
                {
                  "input_references": [
                    {
                      "node_id": "5e66fca5f1e5b88d18f5c23a",
                      "output_id": "words"
                    }
                  ],
                  "name": "positives",
                  "file_type": "json",
                  "values": [],
                  "is_array": true,
                  "min_count": 0
                },
                {
                  "input_references": [
                    {
                      "node_id": "5e66fcc4f1e5b88d18f5c278",
                      "output_id": "words"
                    }
                  ],
                  "name": "negatives",
                  "file_type": "json",
                  "values": [],
                  "is_array": true,
                  "min_count": 0
                }
              ],
              "outputs": [
                {
                  "name": "result",
                  "file_type": "json",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                }
              ],
              "parameters": [
                {
                  "name": "_cmd",
                  "parameter_type": "code",
                  "value": {
                    "value": "import json\nimport pickle\nimport os\n\n\ndef get_words(filenames):\n    res = []\n    for filename in filenames:\n        with open(filename) as f:\n            res.extend(json.load(f))\n    return res\n\npositive = get_words(inputs['positives'])\nnegative = get_words(inputs['negatives'])\n\nwith open(os.path.join('/models', params['model']), 'rb') as f:\n    model = pickle.load(f)\n\nres = model.most_similar(positive=positive, negative=negative)\n\nwith open(outputs['result'], 'w') as f:\n    json.dump(res, f)",
                    "mode": "python"
                  },
                  "mutable_type": false,
                  "removable": false,
                  "publicable": false,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "_cacheable",
                  "parameter_type": "bool",
                  "value": true,
                  "mutable_type": false,
                  "removable": false,
                  "publicable": false,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "_timeout",
                  "parameter_type": "int",
                  "value": 600,
                  "mutable_type": false,
                  "removable": false,
                  "publicable": true,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "model",
                  "parameter_type": "enum",
                  "value": {
                    "values": [
                      "glove-twitter-200",
                      "glove-twitter-25"
                    ],
                    "index": "0"
                  },
                  "mutable_type": true,
                  "removable": true,
                  "publicable": true,
                  "widget": "model",
                  "reference": null
                }
              ],
              "logs": [
                {
                  "name": "stderr",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                },
                {
                  "name": "stdout",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                },
                {
                  "name": "worker",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                }
              ],
              "node_running_status": "CREATED",
              "node_status": "READY",
              "cache_url": "",
              "x": 282,
              "y": 142,
              "author": "5e5dd9c7653752f34e1e0be6",
              "starred": false
            }),
            plynx.db.node.Node.from_dict({
              "_id": "5e66fca5f1e5b88d18f5c23a",
              "title": "Words to list",
              "description": "Positive words",
              "kind": "basic-python-node-operation",
              "parent_node_id": null,
              "successor_node_id": null,
              "original_node_id": "5e66eaafe85256834fda470a",
              "inputs": [],
              "outputs": [
                {
                  "name": "words",
                  "file_type": "json",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                }
              ],
              "parameters": [
                {
                  "name": "_cmd",
                  "parameter_type": "code",
                  "value": {
                    "value": "import json\n\nwith open(outputs['words'], 'w') as f:\n    json.dump(params['words'], f)",
                    "mode": "python"
                  },
                  "mutable_type": false,
                  "removable": false,
                  "publicable": false,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "_cacheable",
                  "parameter_type": "bool",
                  "value": true,
                  "mutable_type": false,
                  "removable": false,
                  "publicable": false,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "_timeout",
                  "parameter_type": "int",
                  "value": 600,
                  "mutable_type": false,
                  "removable": false,
                  "publicable": true,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "words",
                  "parameter_type": "list_str",
                  "value": [
                    "king",
                    "woman"
                  ],
                  "mutable_type": true,
                  "removable": true,
                  "publicable": true,
                  "widget": "words",
                  "reference": null
                }
              ],
              "logs": [
                {
                  "name": "stderr",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                },
                {
                  "name": "stdout",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                },
                {
                  "name": "worker",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                }
              ],
              "node_running_status": "CREATED",
              "node_status": "READY",
              "cache_url": "",
              "x": 30,
              "y": 80,
              "author": "5e5dd9c7653752f34e1e0be6",
              "starred": false
            }),
            plynx.db.node.Node.from_dict({
              "_id": "5e66fcc4f1e5b88d18f5c278",
              "title": "Words to list",
              "description": "Negative words",
              "kind": "basic-python-node-operation",
              "parent_node_id": null,
              "successor_node_id": null,
              "original_node_id": "5e66eaafe85256834fda470a",
              "inputs": [],
              "outputs": [
                {
                  "name": "words",
                  "file_type": "json",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                }
              ],
              "parameters": [
                {
                  "name": "_cmd",
                  "parameter_type": "code",
                  "value": {
                    "value": "import json\n\nwith open(outputs['words'], 'w') as f:\n    json.dump(params['words'], f)",
                    "mode": "python"
                  },
                  "mutable_type": false,
                  "removable": false,
                  "publicable": false,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "_cacheable",
                  "parameter_type": "bool",
                  "value": true,
                  "mutable_type": false,
                  "removable": false,
                  "publicable": false,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "_timeout",
                  "parameter_type": "int",
                  "value": 600,
                  "mutable_type": false,
                  "removable": false,
                  "publicable": true,
                  "widget": null,
                  "reference": null
                },
                {
                  "name": "words",
                  "parameter_type": "list_str",
                  "value": [
                    "man"
                  ],
                  "mutable_type": true,
                  "removable": true,
                  "publicable": true,
                  "widget": "words",
                  "reference": null
                }
              ],
              "logs": [
                {
                  "name": "stderr",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                },
                {
                  "name": "stdout",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                },
                {
                  "name": "worker",
                  "file_type": "file",
                  "values": [],
                  "is_array": false,
                  "min_count": 1
                }
              ],
              "node_running_status": "CREATED",
              "node_status": "READY",
              "cache_url": "",
              "x": 30,
              "y": 225,
              "author": "5e5dd9c7653752f34e1e0be6",
              "starred": false
            }),
        ]

        node.title = 'Word2vec'
        node.title = 'A + B - C example'
        return node
