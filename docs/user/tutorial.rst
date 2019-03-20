Tutorial
=====================

This tutorial shows how generate adversarial examples


Create a model
--------------

For this tutorial, we are using a simple model implemented in pytorch.

.. code-block:: python

    class SimpleModel(nn.Module):
    def __init__(self, dim_input=DIM_INPUT, num_classes=NUM_CLASS):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(dim_input, 10)
        self.fc2 = nn.Linear(10, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x

    NUM_CLASS = 10
    DIM_INPUT = 15
    BATCH_SIZE = 16
    inputs = np.random.uniform(0, 1, size=(BATCH_SIZE, DIM_INPUT))
    targets = np.random.randint(0, NUM_CLASS, size=BATCH_SIZE)
    model_pt = SimpleModel(DIM_INPUT, NUM_CLASS)

    if inputs.ndim == 4:
        # TODO: move the transpose to a better place
        input_t = torch.from_numpy(inputs.transpose(0, 3, 1, 2))
    else:
        input_t = torch.from_numpy(inputs)
    input_t = input_t.float()

    target_t = torch.from_numpy(targets)




Apply the attack
----------------
Here we are taking the LinfPGDAttack (Madry et al, 2017) as example

.. code-block:: python

    adversary = LinfPGDAttack(
        model_pt, clip_min=0., clip_max=1., binary_search_steps=3,
        max_iterations=50, initial_const=1e-3, batch_size=BATCH_SIZE,
        num_classes=NUM_CLASS)

    adversary.targeted = True
    adv_pt = adversary.perturb(input_t, target_t)











