import React from 'react';
import Chart from './Chart';
import styled from 'styled-components';

const Container = styled.div`
	display: flex;
	height: 100%;
	width: 100%;
	flex-direction: column;
`;

const Header = styled.h1`
	text-align: center;
	padding: 25px;
	margin: 25px;
`;

class App extends React.Component {
	state = {
		peoples: [],
	};
	fetchPeoples = async () => {
		const res = await fetch(
			'https://warm-lake-39502.herokuapp.com/peoples',
			{
				mode: 'cors',
			}
		);
		const resJson = await res.json();
		this.setState({ peoples: resJson });
	};

	async componentDidMount() {
		this.fetchPeoples();
		setInterval(async () => {
			this.fetchPeoples();
		}, 1000);
	}
	render() {
		return (
			<Container>
				<Header>Who's enter the room</Header>
				<Chart peoples={this.state.peoples} />
			</Container>
		);
	}
}

export default App;
