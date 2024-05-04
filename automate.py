from roboflow import Roboflow as rb


def roboflow_exec(model):
    output = model.predict("test.png", confidence=55, overlap=30).json()
    return output


def roboflow_init():
    rkey = rb(api_key="rjZHPFB1xcUthxuCcNHH")
    project = rkey.workspace().project("cat-lwvzc")
    model = project.version("2").model
    return model
