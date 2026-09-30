def validate_input(data: Dict) -> Dict:
    for key, value in data.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f'Invalid input type for {key}')
    return data

def sanitize_symbols(symbols: List[str]) -> List[str]:
    return [symbol.upper() for symbol in symbols if symbol.isalpha()]
