
Bonjour {{ user.user.name }},

Ta consommation à l'heure actuelle est de {{ user.nb }} boisson{{ user.nb |pluralize }}.

Si tu souhaites payer et "effacer" cette ardoise, saches que tu dois {{ user.euro|floatformat:2 }} € à la caisse des boissons.

En te remerciant pour ton attention,

Cordialement,

Les admins de drinkmanager.
