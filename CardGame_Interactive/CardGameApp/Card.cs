namespace CardGameApp;

public class Card
{
	private byte _value;
	private CardSuit _suit;

	public Card(byte value, CardSuit suit)
	{
		_value = value;
		_suit = suit;
	}

	public byte Value
	{
		get { return _value; }
		set { _value = value; }
	}

	public CardSuit Suit
	{
		get { return _suit; }
		set { _suit = value; }
	}

	public string CardName
	{
		get
		{
			//TODO: implement CardName
			return "";
		}
	}

	public string SuitName
	{
		get
		{
			//TODO: implement SuitName
			return "";
		}
	}
}
