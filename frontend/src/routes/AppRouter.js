import Details from '../components/details';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

const AppRouter = () => {
    return (
      <Router>
        <Routes>
         <Route path="/" element={<Details/>} />    
        </Routes>
      </Router>
    );
  };
  
  export default AppRouter;