import numpy as np


import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 
print(params.dim_state)
class Filter:
    '''Kalman filter class'''
    def __init__(self):
        self.dim_state = params.dim_state
        self.dt = params.dt
        self.q = params.q
        
        
    def F(self):
        F_matrix = np.matrix([[1, 0, 0, self.dt, 0 ,0],
                              [0, 1, 0, 0, self.dt, 0],
                              [0, 0, 1, 0, 0 , self.dt],
                              [0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 1, 0], 
                              [0, 0, 0, 0, 0, 1]])

        return F_matrix


    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        q1 = ((self.dt**3)/3) * self.q 
        q2 = ((self.dt**2)/2) * self.q 
        q3 = self.dt * self.q 

        Q_matrix = np.matrix([[q1, 0, 0, q2, 0, 0],
                              [0, q1, 0, 0, q2, 0],
                              [0, 0, q1, 0, 0, q2],
                              [q2, 0, 0, q3, 0, 0],
                              [0, q2, 0, 0, q3, 0],
                              [0, 0, q2, 0, 0, q3]])

        return Q_matrix
        

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        Q = self.Q()
        F = self.F()
        P = track.P
        x = track.x

        x = F @ track.x
        P = F @ track.P @ F.transpose() + Q
        
        track.set_P(P)
        track.set_x(x)
        

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        gamma = self.gamma(track=track,meas=meas)

        H = meas.sensor.get_H(track.x)
        S = self.S(track=track,meas=meas,H = H)
        K = track.P @ H.T @ np.linalg.inv(S)

        x = track.x + K @ gamma
        I = np.identity(params.dim_state)
        P = (I - K @ H) @ track.P

        track.set_P(P)
        track.set_x(x)
        track.update_attributes(meas)
    

    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        
        return meas.z - meas.sensor.get_hx(track.x)
        

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        return H @ track.P @ H.transpose() + meas.R