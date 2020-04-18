import React from 'react';
import { FETCHING_DATA, DATA_RECIEVED, DATA_NOT_FOUND } from '../actions/actions';

const initialState = {
    title: "dog lover",
    getting_data: false,
    images: []
    
}
const AnimeReducer = (state = initialState, action) => {
    switch(action.type){
        case FETCHING_DATA:
            return {
                ...state, getting_data: true
            }
        case DATA_RECIEVED:
            
            return {
                ...state, images: action.payload.message
            }

        default:
            return state
    }
}

export default AnimeReducer;
