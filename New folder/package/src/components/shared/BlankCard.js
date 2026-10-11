import { Card } from '@mui/material';
import React from 'react';
import PropTypes from 'prop-types';

const BlankCard = ({ children, className }) => {
  return (
    <Card
      sx={{ p: 0, position: 'relative' }}
      className={className}
      elevation={9}
      variant={undefined}
    >
      {children}
    </Card>
  );
};

BlankCard.propTypes = {
  children: PropTypes.node,
};

export default BlankCard;
