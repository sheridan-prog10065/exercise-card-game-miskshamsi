namespace CardGameApp;

public class CardDeck
{
	private List<Card> _cardList;

	public CardDeck()
	{
		_cardList = new List<Card>();
	}

	public int CardCount
	{
		get { return _cardList.Count; }
	}
}
