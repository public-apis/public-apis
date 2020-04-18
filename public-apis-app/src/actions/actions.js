import axios from 'axios';
export const FETCHING_DATA = "FETCHING_DATA"
export const DATA_RECIEVED = "DATA_RECIEVED"
export const DATA_NOT_FOUND = "DATA_NOT_FOUND"

export const getAnime = (data) => dispatch => {
    dispatch({type:FETCHING_DATA})
    axios
        .get(`https://dog.ceo/api/breed/${data}/images`)
        .then(res => {
            console.log(res)
            dispatch({type:DATA_RECIEVED, payload:res.data})
        })
        .catch(err => {
            console.log(err)
            dispatch({type:DATA_NOT_FOUND, payload:err})
        })
}