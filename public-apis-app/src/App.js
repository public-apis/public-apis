import React, {useState} from 'react';
import './App.css';
import { useForm } from 'react-hook-form';
import { connect } from 'react-redux';
import { getAnime } from './actions/actions';
import DogImages from './DogImages';
import { Div } from './DogImage';

function App(props) {
  const { register } = useForm()
  const [searchQuery, setSearchQuery] = useState('')

  const handleChange = event => {
    setSearchQuery(event.target.value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    props.getAnime(searchQuery)
  }
  return (
    <Div>
      <h1>{props.title}</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="search dogs" name="search" value={searchQuery} onChange={handleChange} ref={register}></input>
        <button type="submit">search</button>
      </form>
      <DogImages/>
    </Div>
  );
}

const mapStateToProps = state => {
  return {
    title: state.title,
  }
}

export default connect(mapStateToProps,{getAnime})(App);
