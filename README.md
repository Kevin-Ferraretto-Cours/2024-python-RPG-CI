# Python RPG - Système d'Intégration Continue

## Équipe

- Gabriel K ([@GabYan876](https://github.com/GabYan876)).
- Kevin F. ([@MrSuricate2](https://kevin-ferraretto.fr/))
- Anis H. ([@tduki](https://github.com/tduki))

## À propos du projet

Ce projet vise à développer un jeu de rôle (RPG) en Python dans le cadre d'un projet scolaire. Une infrastructure d'intégration continue (CI) a été mise en place pour assurer la qualité du code à chaque étape du développement.

## Structure du projet

```
python-rpg/
├── src/                # Dossier contenant les classes du RPG
├── tests/              # Tests unitaires et d'intégration
├── .github/            # Configuration GitHub
│   └── workflows/      # Dossier des workflows GitHub Actions
│       └── blank.yml   # Configuration de l'intégration continue
├── LICENSE             # Fichier de licence MIT
└── README.md           # Documentation du projet
```

## Flux de travail CI/CD

Notre pipeline d'intégration continue est configuré pour fonctionner comme suit:

1. Les développeurs poussent leurs modifications vers la branche `dev`
2. GitHub Actions exécute automatiquement les tests sur la branche `dev`
3. Si les tests réussissent, les modifications sont automatiquement fusionnées dans la branche `main`
4. En cas d'échec des tests:
   - Une branche d'échec temporaire est créée pour référence
   - La branche `dev` est réinitialisée à son état précédent

Ce flux de travail garantit que seul le code fonctionnel et de qualité atteint la branche principale.

## Avantages de notre solution GitHub Actions

### Points forts

- **Intégration native avec GitHub**: Configuration simplifiée et synchronisation directe avec notre dépôt
- **Configuration flexible via YAML**: Personnalisation complète du pipeline selon nos besoins spécifiques
- **Support multi-langages**: Compatibilité avec Python et possibilité d'extension à d'autres langages
- **Accès à des actions préconstruites**: Utilisation d'actions standardisées pour optimiser notre workflow
- **Ressources gratuites**: Utilisation des 10 000 minutes gratuites mensuelles pour notre projet open-source

### Limitations

- **Ressources limitées pour les projets privés**: 2 000 minutes gratuites mensuelles pourraient être insuffisantes pour des projets de grande envergure
- **Performance des runners gratuits**: Puissance de calcul modérée pouvant affecter les temps d'exécution des pipelines complexes
- **Complexité potentielle des fichiers YAML**: Maintenance plus exigeante pour des workflows sophistiqués
- **Écosystème limité à GitHub**: Non compatible avec d'autres plateformes de gestion de code

## Installation et utilisation

### Prérequis

- Python 3.12 ou version ultérieure
- pytest

### Exécution des tests locaux

```bash
pip install pytest
pytest
```

### Contribution

1. Créez une branche à partir de `dev`
2. Implémentez vos modifications
3. Ajoutez des tests pour vos nouvelles fonctionnalités
4. Soumettez une pull request vers la branche `dev`
5. Attendez la validation de la CI avant le merge vers `main`

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
