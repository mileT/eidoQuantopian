# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:29:00 2016

@author: jhan
"""

function [TP_median1, TN_median1, FP_median1, FN_median1, HR_median1,  TP_unc1, TN_unc1, FP_unc1, FN_unc1, HR_unc1, TP_median2, TN_median2, FP_median2, FN_median2, HR_median2 ,TP_unc2, TN_unc2, FP_unc2, FN_unc2, HR_unc2,  r_mean, p_mean,r_median, p_median,  rs_mean, ps_mean,rs_median, ps_median, MSE_mean, MAE_mean,MSE_median, MAE_median, num_forecasts, DecileSpread, VigSpread, PerSpread ] = AnalysisFromFile( filename, unc_median)

% Load  a stats file and calculate a large set of forecasting metrics
% Inputs: filename: name of stats file
%   unc_median: median of unconditional space used in hit rate calculations
%Outputs:
% TP_median1: number of True positives (guess up, actual is up) using the  conditional median as a forecast and ignoring
% zero forecast and outcomes
% TN_median1: True negatives (guess down, actual is down) using the conditional median as a forecast and ignoring
% zero forecast and outcomes
% FP_median1: Flase positives (guess down, actual is up) using the conditional median as a forecast and ignoring
% zero forecast and outcomes
% FN_median1: False negatives (guess up, actual is down) using the conditional median as a forecast and ignoring
% zero forecast and outcomes
% HR_median1: hit rate using the conditional median as a forecast and ignoring
% zero forecast and outcomes
% TP_unc1: number of True positives (guess up, actual is up) using the  unconditional median as a forecast and ignoring
% zero forecast and outcomes
% TN_unc1: True negatives (guess down, actual is down) using the unconditional median as a forecast and ignoring
% zero forecast and outcomes
2% FP_unc1: Flase positives (guess down, actual is up) using the unconditional median as a forecast and ignoring
% zero forecast and outcomes
% FN_unc1: False negatives (guess up, actual is down) using the unconditional median as a forecast and ignoring
% zero forecast and outcomes
% HR_unc1: hit rate using the unconditional median as a forecast and ignoring
% zero forecast and outcomes
% TP_median2: number of True positives (guess up, actual is up) using the
% conditional median as a forecast and counting zero forecasts and outcomes
% as Up
% TN_median2: True negatives (guess down, actual is down) using the conditional median as a forecast and counting zero forecasts and outcomes
% as Up
% FP_median2: Flase positives (guess down, actual is up) using the conditional median as a forecast and counting zero forecasts and outcomes
% as Up
% FN_median2: False negatives (guess up, actual is down) using the conditional median as a forecast and counting zero forecasts and outcomes
% as Up
% HR_median2: hit rate using the conditional median as a forecast and counting zero forecasts and outcomes
% as Up
% TP_unc2: number of True positives (guess up, actual is up) using the
% unconditional median as a forecast and counting zero forecasts and outcomes
% as Up
% TN_unc2: True negatives (guess down, actual is down) using the unconditional median as a forecast and counting zero forecasts and outcomes
% as Up
% FP_unc2: Flase positives (guess down, actual is up) using the unconditional median as a forecast and counting zero forecasts and outcomes
% as Up
% FN_unc2: False negatives (guess up, actual is down) using the unconditional median as a forecast and counting zero forecasts and outcomes
% as Up
% HR_unc2: hit rate using the unconditional median as a forecast and counting zero forecasts and outcomes
% as Up
% r_mean: Pearson correlation of conditional mean from mean column in file with the actual retursn
% p_mean: p-value of r_mean
% r_median:Pearson correlation of conditional median from median column in file with the actual returns 
% p_median: p_value of r_median
% rs_mean: Spearman correlation of conditional mean from mean column in file with the actual retursn
% ps_mean: p-value of rs_mean
% rs_median: Spearman correlation of conditional median from median column in file with the actual returns 
% ps_median: p_value of rs_median
% MSE_mean: sum of squared errors (mean-actaul), 
% MAE_mean: sum of absolute errors (mean-actual)
% MSE_median: sum of squared errors (median-actaul)
% MAE_median: sum of absolute errors (median-actual)
% num_forecasts: total number of forecasts made, a low number can indicate few matches were found in many cases
% DecileSpread: rank the forecasts by highest projected mean then look at the actual returns of the top 10% - actual returns of the bottom 10%
% VigSpread: rank the forecasts by highest projected mean then look at the actual returns of the top 5% - actual returns of the bottom 5%
% PerSpread: rank the forecasts by highest projected mean then look at the actual returns of the top 5% - actual returns of the bottom 5%


% import file
[patternID,endDate,actualReturn,mean1,variance,median,upside,downside,num_results] = import_stats_file(filename);
% pearson correlation
[r_mean, p_mean]=corr(mean1, actualReturn, 'rows', 'complete', 'tail', 'right');
[r_median, p_median]=corr(median, actualReturn, 'rows', 'complete', 'tail', 'right');

% spearman correaltion
[rs_mean, ps_mean]=corr(mean1, actualReturn, 'rows', 'complete', 'type', 'spearman', 'tail', 'right');
[rs_median, ps_median]=corr(median, actualReturn, 'rows', 'complete', 'type', 'spearman', 'tail', 'right');

% number of lines in the file
num_forecasts=length(mean1);

% calculate hit rate and 2d confusion matrix
[ TP_median1, TN_median1, FP_median1, FN_median1, HR_median1 ] = HitRate( median, actualReturn, 1 );
[ TP_median2, TN_median2, FP_median2, FN_median2, HR_median2 ] = HitRate( median, actualReturn, 2 );
[ TP_unc1, TN_unc1, FP_unc1, FN_unc1, HR_unc1 ] = HitRate( unc_median*ones(num_forecasts,1), actualReturn, 1 );
[ TP_unc2, TN_unc2, FP_unc2, FN_unc2, HR_unc2 ] = HitRate( unc_median*ones(num_forecasts,1), actualReturn, 2 );

% MSE
MSE_mean=sum((actualReturn-mean1).^2)/length(mean1);
MSE_median=sum((actualReturn-median).^2)/length(median);

%MAE
MAE_mean=sum(abs(actualReturn-mean1))/length(mean1);
MAE_median=sum(abs(actualReturn-median))/length(median);

% caluclate spreads from sorted array
t_array=[mean1 actualReturn];
sortedArray=sortrows(t_array,1);
q_size=floor(length(mean1)/10);
DecileSpread=nanmean(sortedArray(end-q_size+1:end,2)) - nanmean(sortedArray(1:q_size,2));
q_size=floor(length(mean1)/20);
VigSpread=nanmean(sortedArray(end-q_size+1:end,2)) - nanmean(sortedArray(1:q_size,2));
q_size=floor(length(mean1)/100);
PerSpread=nanmean(sortedArray(end-q_size+1:end,2)) - nanmean(sortedArray(1:q_size,2));

end

