#!/bin/bash

# --- 🎨 PALETTE DE COULEURS ---
RESET='\033[0m'
BOLD='\033[1m'

# Couleurs de texte
BLUE='\033[34m'
MAGENTA='\033[35m'
CYAN='\033[36m'
GREEN='\033[32m'

# Chemins relatifs
PROGRAM="computor_bonus.py"

# Fonction générique d'exécution
run_test() {
    PROG=$1
    DESC=$2
    EXPR=$3
    COLOR=$4
    
    echo -e "${COLOR}Test : $DESC${RESET}"
    echo -e "Input : $EXPR"
    echo -e "${BOLD}Output :${RESET}"
    python3 "$PROG" "$EXPR"
    echo ""
}

# clear   # desactive : effacerait la sortie precedente en soutenance

# ==========================================================
# 🛡️  PARTIE 1 : VÉRIFICATION DU MANDATORY
# ==========================================================

if [ ! -f "$PROGRAM" ]; then
    echo "⚠️  Erreur : Impossible de trouver $PROGRAM"
else
    echo -e "${BOLD}${BLUE}=== PARTIE 1 : MANDATORY =================================${RESET}\n"

    # On teste que le code de base fonctionne toujours correctement
    run_test "$PROGRAM" "Classique (Delta > 0)" "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" "$BLUE"
    run_test "$PROGRAM" "Degré 1" "5 * X^0 + 4 * X^1 = 4 * X^0" "$BLUE"
fi

# ==========================================================
# 🚀  PARTIE 2 : FONCTIONNALITÉS BONUS
# ==========================================================

if [ ! -f "$PROGRAM" ]; then
    echo "⚠️  Erreur : Impossible de trouver $PROGRAM"
else
    echo -e "${BOLD}${MAGENTA}=== PARTIE 2 : BONUS =====================================${RESET}"
    echo -e "${MAGENTA}Features : Forme libre, autre a suivre${RESET}\n"

    # 1. Test du Parsing intelligent
    run_test "$PROGRAM" "Forme Libre (X^2 + 4X = 5)" "X^2 + 4X = 5" "$MAGENTA"
    
    # 2. Test du mélange et signes
    run_test "$PROGRAM" "Ordre mélangé (5 - X = X^2)" "5 - X = X^2" "$MAGENTA"

fi

# ==========================================================
# ➗  PARTIE 3 : AFFICHAGE FRACTIONNAIRE
# ==========================================================

if [ ! -f "$PROGRAM" ]; then
    echo "⚠️  Erreur : Impossible de trouver $PROGRAM"
else
    echo -e "${BOLD}${CYAN}=== PARTIE 3 : BONUS (Fractions Irréductibles) ===${RESET}"
    echo -e "${CYAN}Features : PGCD, Simplification, Affichage conditionnel${RESET}\n"

    # 1. Degré 1 (Fraction simple)
    # 4X = 3 -> X = 0.75 ou 3/4
    run_test "$PROGRAM" "Degré 1 (3/4)" "4X = 3" "$CYAN"

    # 2. Degré 2 (Delta = 0, Entier)
    # (X+1)^2 -> X = -1
    run_test "$PROGRAM" "Delta Null (Entier -1)" "X^2 + 2X + 1 = 0" "$CYAN"

    # 3. Degré 2 (Delta < 0, Complexe Entier)
    # X^2 + 1 = 0 -> +/- i
    run_test "$PROGRAM" "Complexe Pur (i)" "X^2 + 1 = 0" "$CYAN"

    # 4. Degré 2 (Delta > 0, Moche - Pas de fraction)
    # X^2 + 4X + 1 = 0 -> Racine de 12 (irrationnel) -> Pas de fraction affichée
    run_test "$PROGRAM" "Irrationnel (Pas de fraction)" "X^2 + 4X + 1 = 0" "$CYAN"
fi

echo -e "${BOLD}${GREEN}✅ Fin de la suite de tests.${RESET}"