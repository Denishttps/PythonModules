from __future__ import annotations

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        score1 = card1.attack_power + card1.health + card1.rating
        score2 = card2.attack_power + card2.health + card2.rating

        winner = card1 if score1 >= score2 else card2
        loser = card2 if winner is card1 else card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        ordered = sorted(
            self.cards.values(),
            key=lambda card: (-card.rating, card.name),
        )
        return [
            {
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}",
            }
            for card in ordered
        ]

    def generate_tournament_report(self) -> dict:
        if not self.cards:
            avg_rating = 0
        else:
            avg_rating = sum(
                card.rating for card in self.cards.values()
            ) // len(self.cards)
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
