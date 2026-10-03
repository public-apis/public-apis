import React from 'react';
import { Grid, Box, Card, Typography, Stack } from '@mui/material';
import { Link } from 'react-router-dom';
import PageContainer from 'src/components/container/PageContainer';
import Logo from 'src/layouts/full/shared/logo/Logo';
import AuthRegister from './auth/AuthRegister';

const Register2 = () => (
  <PageContainer title="Register" description="this is Register page">
    <Box
      sx={{
        position: 'relative',
        '&:before': {
          content: '""',
          background: 'radial-gradient(#d2f1df, #d3d7fa, #bad8f4)',
          backgroundSize: '400% 400%',
          animation: 'gradient 15s ease infinite',
          position: 'absolute',
          height: '100%',
          width: '100%',
          opacity: '0.3',
        },
      }}
    >
      <Grid container spacing={0} justifyContent="center" sx={{ height: '100vh' }}>
        <Grid
          item
          xs={12}
          sm={12}
          lg={4}
          xl={3}
          display="flex"
          justifyContent="center"
          alignItems="center"
        >
          <Card elevation={9} sx={{ p: 4, zIndex: 1, width: '100%', maxWidth: '500px' }}>
            <Box display="flex" alignItems="center" justifyContent="center">
              <Logo />
            </Box>
            <AuthRegister
              subtext={
                <Typography variant="subtitle1" textAlign="center" color="textSecondary" mb={1}>
                  Your Social Campaigns
                </Typography>
              }
              subtitle={
                <Stack direction="row" justifyContent="center" spacing={1} mt={3}>
                  <Typography color="textSecondary" variant="h6" fontWeight="400">
                    Already have an Account?
                  </Typography>
                  <Typography 
                    component={Link}
                    to="/auth/login"
                    fontWeight="500"
                    sx={{
                      textDecoration: 'none',
                      color: 'primary.main',
                    }}
                  >
                    Sign In
                  </Typography>
                </Stack>
              }
            />
          </Card>
        </Grid>
      </Grid>
    </Box>
  </PageContainer>
);

export default Register2;
