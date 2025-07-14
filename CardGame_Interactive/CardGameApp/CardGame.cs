namespace CardGameApp;

public class CardGame
{
	private CardDeck _cardDeck;
	private GameScore _score;
	private Card _playerCard;
	private Card _houseCard;

	public CardGame()
	{
		_cardDeck = new CardDeck();
		_score = new GameScore();
		_playerCard = null;
		_houseCard = null;
	}
	
	public GameScore Score
	{
		get { return _score; }
	}

	public Card PlayerCard
	{
		get { return _playerCard; }
	}

	public Card HouseCard
	{
		get { return _houseCard; }
	}

	public bool PlayerWins
	{
		get
		{
			//TODO: implmeent PlayerWins 
			return false;
		}
	}

	public bool HouseWins
	{
		get
		{
			//TODO: Implement HouseWins
			return false;
		}
	}

	public bool IsOver
	{
		get
		{
			//TODO: implment this
			return false;
		}
	}


}
