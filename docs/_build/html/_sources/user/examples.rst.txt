Examples
=====================

Here is an example of using LinfPGDAttack.

.. code-block:: python

   # prepare your pytorch model as "model"
   # prepare a batch of data and label as "cln_data" and "true_label"
   # ...
   from advertorch.attacks import LinfPGDAttack
   adversary = LinfPGDAttack(
       model, loss_fn=nn.CrossEntropyLoss(reduction="sum"), eps=0.3,
       nb_iter=40, eps_iter=0.01, rand_init=True, clip_min=0.0, clip_max=1.0,
       targeted=False)
   adv_untargeted = adversary.perturb(cln_data, true_label)
   target = torch.ones_like(true_label) * 3
   adversary.targeted = True
   adv_targeted = adversary.perturb(cln_data, target)
