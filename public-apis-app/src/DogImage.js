import React from 'react';
import styled from 'styled-components';

const Img = styled.img`
    width: 300px;
    height: 300px;
`
export const Div = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 20px;
`

const DogImage = (props) => {
    return (
        <Div>
            <Img src={props.image}/>
        </Div>
    );
}

export default DogImage;
