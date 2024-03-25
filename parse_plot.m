% Read the data from the text file
data = importdata('2024-03-20 16%3A52%3A11.024006.txt'); 

% Extract the data columns
channel = data.data(:, 1);
voltage = data.data(:, 2);
time = data.data(:, 3);

ADC_CHANNELS = max(channel);

%Plot while Computing
figure;
for adc = 0:ADC_CHANNELS
    % find is cool function. Should use later.
    indices = find(channel == adc);
    
    subplot(2, 2, adc + 1);
    plot(time(indices), voltage(indices), 'o-');
    
    xlabel('Time (S)');
    ylabel('Voltage (V)');
    title(['ADC Channel:' num2str(adc)]);
    grid on;
end
