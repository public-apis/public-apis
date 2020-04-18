import React from 'react';
import { connect } from 'react-redux';
import DogImage from './DogImage';

const DogImages = (props) => {
    return (
        <div>
            {props.dogs.map((image,i) => {
                return <DogImage key={i} image={image}/>
            })}
        </div>
    )
 }

const mapStateToProps = state => {
    return {
        dogs: state.images
    }
}
export default connect(mapStateToProps,{})(DogImages);
