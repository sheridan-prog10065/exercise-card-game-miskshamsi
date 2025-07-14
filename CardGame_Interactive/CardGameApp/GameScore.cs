namespace CardGameApp;

public struct GameScore
{
	private int _playerScore;
	private int _houseScore;

	public GameScore(int playerScore, int houseScore)
	{
		_playerScore = playerScore;
		_houseScore = houseScore;
	}

	public int PlayerScore
	{
		get { return _playerScore; }
		set { _playerScore = value; }
	}

	public int HouseScore
	{
		get { return _houseScore; }	
		set { _houseScore = value; }
	}

}
