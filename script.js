{
    // custom isNaN
    const customIsNaN = num => num != num; 

    // -0
    const isNegativeZero = num => num === -0 && 1 / num === Number.NEGATIVE_INFINITY;

    // isEven and isOdd (!isEven)
    const isEven = num => 1n != (BigInt(num) & 1n);

    // isPrime function 
    const isPrime = num => {
        for(let i = 2, s = Math.sqrt(num); i <= s; i++) {
            if(num % i === 0) return false;
        }

        return num > 1;
    };

    // isHex
    const isHex = value => Boolean(value.match(/^0x[0-9a-f]+$/i));

    // isOctal
    const isOctal = value => Boolean(value.match(/^0o[0-7]+$/i));
      
    // isBinary
    const isBinary = value => Boolean(value.match(/^0b[0-1]+$/i));

    // custom isArray
    const customIsArray = value => value && typeof value === 'object' && value.constructor === Array;

    // isInfinity
    const isInfinity = num => num === Number.NEGATIVE_INFINITY || num === Number.POSITIVE_INFINITY;
       
    // isObject
    const isObject = value => value && typeof value === 'object' && value.constructor === Object;

    // isSafeInteger
    const customIsSafeInteger = num => !isFloat(num) && Math.abs(num) <= Number.MAX_SAFE_INTEGER;

    // isFloat
    const isFloat = num => num && typeof num === 'number' && num !== Math.floor(num);
    
    // isNegativeNumber
    const isNegativeNumber = num => num < 0 || isNegativeZero(num);

    // custom sign
    const customSign = num => num > 0 ? 1 : num < 0 ? -1 : num === 0 ? 0 : NaN;


    // power of two
    const isPowerOfTwo = num => num > 0 && (num & (num - 1)) === 0;
    
    // power of three
    const isPowerOfThree = (num) => {
        if (num <= 0) return false; 
        
        while (num % 3 === 0) {
            num /= 3;
        }

        return num === 1;
    };

    Object.defineProperties(Number, {
        customIsNaN: {
            value: customIsNaN
        },
        isNegativeZero: {
            value: isNegativeZero
        },
        isEven: {
            value: num => Number.isInteger(num) && isEven(num)
        },
        isOdd: {
            value: num => Number.isInteger(num) && !isEven(num)
        },
        isPrime: {
            value: isPrime
        },
        isHex: {
            value: isHex
        },
        isOctal: {
            value: isOctal
        },
        isBinary: {
            value: isBinary
        },
        isInfinity: {
            value: isInfinity
        },
        customIsSafeInteger: {
            value: customIsSafeInteger
        },
        isFloat: {
            value: isFloat
        },
        isNegativeNumber: {
            value: isNegativeNumber
        },
        customSign: {
            value: customSign
        },
        isPowerOfTwo: {
            value: isPowerOfTwo
        },
        isPowerOfThree: {
            value: isPowerOfThree
        }
    });

    Object.defineProperties(BigInt, {
        isEven: {
            value: num => typeof num === 'bigint' && isEven(num)
        },
        isOdd: {
            value: num => typeof num === 'bigint' && !isEven(num)
        },
    });

    Object.defineProperties(Array, {
        customIsArray: {
            value: customIsArray
        },
    });

    Object.defineProperties(Object, {
        isObject: {
            value: isObject
        },
    });
}


