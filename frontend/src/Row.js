import React from 'react';
import styled from 'styled-components';

const Container = styled.div`
	/* flex: 1; */
	display: flex;
	margin: 10px;
	padding: 10px;
	width: 80%;
	flex-direction: column;
	border-radius: 20px;
	background-color: #fafafa;

	-webkit-box-shadow: 7px 7px 26px -4px rgba(125, 125, 125, 1);
	-moz-box-shadow: 7px 7px 26px -4px rgba(125, 125, 125, 1);
	box-shadow: 7px 7px 26px -4px rgba(125, 125, 125, 1);
`;

const NameContainer = styled.p`
	margin: 5px;
	padding: 5px;
	font-size: 22px;
	font-weight: 500;
`;

const TimeContainer = styled.p`
	margin: 5px;
	padding: 5px;
`;

class Row extends React.Component {
	render() {
		const date = new Date(this.props.info.lastEnter);
		const now = new Date();
		const difference = now - date;
		let timeDisplay,
			unit = 'วินาที';
		if (difference / 1000 > 1 && difference / 1000 < 60) {
			timeDisplay = Math.floor((now - date) / 1000);
		} else if (difference / 1000 >= 60 && difference / 1000 < 3600) {
			timeDisplay = Math.floor((now - date) / 1000 / 60);
			unit = 'นาที';
		} else if (difference / 1000 >= 3600 && difference / 1000 < 86400) {
			timeDisplay = Math.floor((now - date) / 1000 / 60 / 60);
			unit = 'ชั่วโมง';
		} else {
			timeDisplay = Math.floor((now - date) / 1000 / 60 / 60 / 24);
			unit = 'วัน';
		}
		if (!this.props.info) return <React.Fragment />;
		return (
			<Container>
				<NameContainer>{this.props.info.name}</NameContainer>
				<TimeContainer>{'พบล่าสุด ' + timeDisplay + ' ' + unit + 'ที่แล้ว'}</TimeContainer>
			</Container>
		);
	}
}

export default Row;
