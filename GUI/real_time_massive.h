 #ifndef SUPER_REAL_TIME_H
 #define SUPER_REAL_TIME_H

int gpio_res; 
spi_t *spi;
gpio_t *gpio_in;
uint8_t buf[27]={0};
uint8_t zero27[27]={0x00};
//uint32_t package [8]={0};  



static uint32_t  package_massive [2000]={0}; 


uint ildar[8] = {0,1,2,3,4,5,6,7};  

    
uint32_t data_test = 0x7FFFFF;
uint32_t data_check = 0xFFFFFF;
uint8_t zero3[3] = {0x00, 0x00,0x00}; 
uint8_t zero1[1] = {0x00};



           void write_reg(uint8_t reg_address, uint8_t val_hex)
           {                                            
           uint8_t reg_address_shift = 0x40 | reg_address;
           uint8_t write [3] = {reg_address_shift, 0x00,val_hex};
           int spi_reg = spi_transfer (spi, write, zero3, 3);
           }
           
         void send_command(uint8_t command)
           {           
           uint8_t write_command [1] = {command};                    
           spi_transfer (spi, write_command, zero1, 1);

           }  

        void prepare ()
        {

                                         
        spi = spi_new();
        spi_open_advanced(spi, "/dev/spidev0.0", 0x01, 1000000, MSB_FIRST, 8, 1);   //spi_open_advanced(spi, "/dev/spidev0.0", 0x01, 4000000, MSB_FIRST, 8, 1);        
          
        gpio_in = gpio_new();
        gpio_open (gpio_in, "/dev/gpiochip0", 26, GPIO_DIR_IN);
        gpio_set_edge (gpio_in, GPIO_EDGE_FALLING);  
                                             
          write_reg (0x14,0x80);//led
          write_reg (0x05,0x00);//ch1
          write_reg (0x06,0x01);//ch2
          write_reg (0x07,0x01);//ch3
          write_reg (0x08,0x01);//ch4
          
           write_reg (0x0D,0xFF);//bias N          
           write_reg (0x0E,0x00);//bias P
          
          write_reg (0x09,0x01);//ch5
          write_reg (0x0A,0x01);//ch6
          write_reg (0x0B,0x01);//ch7
          write_reg (0x0C,0x01);//ch8
          write_reg (0x15,0x20);// mics
          write_reg (0x01,0x96);// reg1
          write_reg (0x02,0xD4);// reg2 
          write_reg (0x03,0xE0);// reg3
          send_command (0x10);//sdatc
          send_command (0x08);//start
          
        }

   
                
   extern int *real () 
   { 
     int c = 0;
     int *iru;
     static uint32_t  package [8]={0}; 
     for (int b=0; b<500;b++)
   {
        int timeout = 1000;
        gpio_res = gpio_poll (gpio_in, timeout);  
        
        if (gpio_res == 1)
        {   
            gpio_edge_t edge = GPIO_EDGE_NONE;
            gpio_read_event (gpio_in, &edge, NULL);
            spi_transfer (spi, zero27, buf, 27);
            
            if (buf[0]==192)
            {  
                for (int i = 1; i<9; i++)  
                {                                
                int offset = 3*i;
                int32_t voltage = (buf[offset] << 8) | buf[offset+1];
                voltage = (voltage << 8) | buf[offset+2];


                uint32_t voltage_test = voltage | data_test;

                    if (voltage_test == data_check)
                    {
                    voltage = 16777214 - voltage;                   
                    }
                    package_massive[c]=0.27*voltage;
                    c=c+1;
                    }
                      
            }
          
        } 
                if (c>2000)
                     {  
                       c=0;
                       iru = package_massive;
                       return (iru);
                     } 
    }       

    }
   #endif
