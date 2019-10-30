import React from 'react';
import styled from 'styled-components';
import Row from './Row';

const Container = styled.div`
	display: flex;
	height: 100%;
	flex-direction: column;
	align-items: center;
`;

class Chart extends React.Component {
	render() {
		console.log(this.props);
		return (
			<Container>
				{this.props.peoples.map((people, index) => {
					return <Row info={people} key={index} />;
				})}
			</Container>
		);
	}
}

export default Chart;
