import streamlit as st
import random

# Definir las cartas y sus valores
suits = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Función para crear un mazo de cartas
def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Función para calcular la puntuación de una mano
def calculate_score(hand):
    score = sum(values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    
    while score > 21 and aces:
        score -= 10
        aces -= 1
        
    return score

# Función para mostrar la mano
def display_hand(hand):
    return ', '.join([f'{rank} de {suit}' for rank, suit in hand])

# Inicialización del juego
if 'deck' not in st.session_state:
    st.session_state.deck = create_deck()
    st.session_state.player_hand = []
    st.session_state.dealer_hand = []
    st.session_state.game_over = False
    st.session_state.result = ""

# Inicio del juego
st.title('21 Blackjack')

if st.button('Repartir cartas'):
    if st.session_state.game_over:
        st.session_state.deck = create_deck()
        st.session_state.player_hand = []
        st.session_state.dealer_hand = []
        st.session_state.game_over = False
        st.session_state.result = ""
    
    st.session_state.player_hand = [st.session_state.deck.pop(), st.session_state.deck.pop()]
    st.session_state.dealer_hand = [st.session_state.deck.pop(), st.session_state.deck.pop()]

# Mostrar manos
# Mostrar manos
if st.session_state.player_hand and st.session_state.dealer_hand:
    st.write('Mano del Jugador:', display_hand(st.session_state.player_hand))
    st.write('Mano del Dealer:', f'{st.session_state.dealer_hand[0][0]} de {st.session_state.dealer_hand[0][1]}, ?')
else:
    st.write('Presiona "Repartir cartas" para comenzar el juego.')

# Botón para pedir carta
if st.button('Pedir carta'):
    st.session_state.player_hand.append(st.session_state.deck.pop())
    player_score = calculate_score(st.session_state.player_hand)
    
    if player_score > 21:
        st.session_state.game_over = True
        st.session_state.result = "Te pasaste de 21. ¡Perdiste!"

# Botón para plantarse
if st.button('Plantarse'):
    st.session_state.game_over = True
    dealer_score = calculate_score(st.session_state.dealer_hand)
    
    while dealer_score < 17:
        st.session_state.dealer_hand.append(st.session_state.deck.pop())
        dealer_score = calculate_score(st.session_state.dealer_hand)
    
    player_score = calculate_score(st.session_state.player_hand)
    
    if dealer_score > 21 or player_score > dealer_score:
        st.session_state.result = "¡Ganaste!"
    elif player_score < dealer_score:
        st.session_state.result = "¡Perdiste!"
    else:
        st.session_state.result = "¡Empate!"

# Mostrar el resultado final
if st.session_state.game_over:
    st.write('Mano del Dealer:', display_hand(st.session_state.dealer_hand))
    st.write(st.session_state.result)
